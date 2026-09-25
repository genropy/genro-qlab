class Menu(object):
    def config(self, root, **kwargs):
        components = root.branch('Components')
        components.webpage('Record picker', filepath='/qlab/components/recordpicker')
        root.packageBranch('Administration', tags='admin', pkg='adm')
        root.packageBranch('System', tags='admin', pkg='sys')
