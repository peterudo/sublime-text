import sublime_plugin


class ClearTrailingSpacesOnSave(sublime_plugin.EventListener):

    def on_pre_save(self, view):
        view.run_command('delete_trailing_spaces')
