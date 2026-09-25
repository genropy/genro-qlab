#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='qlab package',sqlschema='qlab',sqlprefix=True,
                    name_short='Qlab', name_long='Qlab', name_full='Qlab')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
