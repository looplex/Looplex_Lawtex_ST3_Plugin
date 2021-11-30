import os
from zipfile import ZipFile

class MyZipFile(ZipFile):

    def extract(self, member, path=None, pwd=None):

        if not isinstance(member, ZipInfo):
            member = self.getinfo(member)

        targetpath = super()._extract_member(member, targetpath, pwd)

        attr = member.external_attr >> 16

        if attr != 0:
            os.chmod(targetpath, attr)

        return targetpath
