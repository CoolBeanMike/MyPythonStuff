#!/usr/bin/python

"""
#
# windowsNTFSworkload.py
#
# This test was written originally to uncover issues with NTFS on seSparse vmdk format which could
# cause corruption of the NTFS filesystem.  This is due to vmware doing defragmentation underneath
# the windows filesystem and modifying the NTFS layout.  This test likely is also useful as a linux
# workload when file creation/verification/deletion is needed.
#
# For the NTFS/seSparse test case the intention is the windows guest will be set up with a second
# virtual disk with the following properties:
#   * 2TB (or greater) in size
#   * thin provisioned
#   * at least one snapshot (which creates the seSparse vmdk as the delta image)
#   * mounted in windows as drive e:
#
# The windows guest VM should have up to date VMware tools installed as this works in conjunction
# with the live VM seSparse defragmentation.  Without the tools corruption is possible but (we believe)
# only as part of a reboot of the guest OS.
#
"""

import os
import sys
import argparse
import random
import time


class FileInfo:
    def __init__(self, rootpath, chunks, chunksize, seed):
        self.path = '%s/testfile_%d' % (rootpath, seed)
        self.chunks = chunks
        self.chunksize = chunksize
        self.seed = seed
        fd = open(self.path, 'w')
        randomizer = random.Random(self.seed)
        offset = 0
        while offset < chunks*self.chunksize:
            fd.write(self._mkchunk(randomizer, offset))
            offset += self.chunksize
        fd.close()

    def deletefile(self):
        try:
            for retry in range(0, 3):
                os.unlink(self.path)
                break
        except WindowsError as e:
            print('error unlinking %s - %s') % self.path,e
            time.sleep(0.5)
            continue
        else:
            print('giving up unlinking %s') % self.path


  def __str__(self):
      return '%s chunks:%d' %(self.path, self.chunks)

  def verify(self):
    fd = open(self.path, 'r')
    randomizer = random.Random(self.seed)
    offset = 0
    while offset < self.chunks*self.chunksize:
      actual = fd.read(self.chunksize)
      expected = self._mkchunk(randomizer, offset)
      self._verifyChunk(offset, actual, expected)
      offset += self.chunksize
      fd.close()
    return


  def _mkchunk(self, randomizer, offset):
      return ("file:%s offset:%s randomtag:%d" % (self.path, offset, randomizer.randint(0, sys.maxint))).ljust(self.chunksize)


  def _verifyChunk(self, offset, actual, expected):
    # TODO: make this more informative... for now just print the data (which might be gibberish if corrupted)
    if actual != expected:
      print('DATA CORRUPTION!  file:%s offset%d' % (self, offset))
      print('expected:%s') % expected
      print('actual  :%s') % actual
      raise AssertionError('DATA CORRUPTION!  file:%s offset%d' % (self.path, offset))


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--chunksize', type=int, default=4096, help="allocation size of verifiable chunk")
  parser.add_argument('--minfilechunks', type=int, default=512, help="minimum size of file in --chunksize units")
  parser.add_argument('--maxfilechunks', type=int, default=8192, help="maximum size of file in --chunksize units")
  parser.add_argument('--maxfiles', type=int, default=300, help="total number of files to create")
  parser.add_argument('--minfiles', type=int, default=200, help="min number of files to keep around")
  parser.add_argument('--runtime', type=float, default=60, help="time in minutes to run")
  parser.add_argument('--seed', type=int, default=int(time.time()))
  parser.add_argument('--rootpath', type=str, default='C:')
  args = parser.parse_args()
  fileList = []
  print('populating with data files....')
  seed=args.seed
  mainrandomizer = random.Random(args.seed)
  end_time = time.time() + args.runtime*60
  try:
    while time.time() < end_time:
      print('current files: %d') % len(fileList)
      chunks = mainrandomizer.randrange(args.minfilechunks, args.maxfilechunks)
      newfile = FileInfo(args.rootpath, chunks, args.chunksize, seed)
      print('created file: %s') % newfile
      fileList.append(newfile)
      seed += 1
      if len(fileList) > args.minfiles:
        verifyfile = mainrandomizer.choice(fileList)
        print('verifying file: %s') % verifyfile
        verifyfile.verify()
      if len(fileList) >= args.maxfiles:
        while len(fileList) > args.minfiles:
          fileToRemove = mainrandomizer.choice(fileList)
          print('removing file: %s') % fileToRemove
          fileToRemove.deletefile()
          fileList.remove(fileToRemove)
  except KeyboardInterrupt:
    print('terminating on ^c')

"""
end of while time loop OR ^c pressed
delete all files, after each file is removed choose another random one to verify
"""
print("")
print('Cleanup up and final verification....')
print("")
while len(fileList) > 0:
    print('current files: %d') % len(fileList)
    verifyfile = mainrandomizer.choice(fileList)
    print('verifying file: %s') % verifyfile
    verifyfile.verify()
    fileToRemove = mainrandomizer.choice(fileList)
    print('removing file: %s') % fileToRemove
    fileToRemove.deletefile()
    fileList.remove(fileToRemove)
    print('done.')
