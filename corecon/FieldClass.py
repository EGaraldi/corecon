

###############
# Field CLASS #
###############

class _Field(dict):
    def __init__(self, *arg, **kw):
        super(_Field, self).__init__(*arg, **kw)

    def get_all_references(self):
        refs = []
        for k in self.keys():
            refs.append( self[k].reference )
        return refs

    def get_all_urls(self):
        urls = []
        for k in self.keys():
            urls.append( self[k].url )
        return urls


