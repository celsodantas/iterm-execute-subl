import sublime, sublime_plugin
from .helper import Helper

class ItermExecuteRunCurrentContextCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    for region in self.view.sel():
      if not region.empty():
        selected_text = self.view.substr(region)
        title = Helper.get_test_title(selected_text)

        if title is not None:
          formated_title = Helper.turn_text_to_regex(title)
          current_file_path = Helper.file_name_from_project(self.view.file_name(), Helper.first_project_path())

          Helper.run_cmd("bundle exec ruby -I test "+ current_file_path + " -n /"+ formated_title +"/")
        else:
          sublime.status_message("iTerm Execute: No test title selected.")
      else:
        sublime.status_message("iTerm Execute: No test title selected.")

class ItermExecuteRunCurrentFileCommand(sublime_plugin.TextCommand, sublime_plugin.WindowCommand):

  def run(self, edit):
    current_file_path = Helper.file_name_from_project(self.view.file_name(), Helper.first_project_path())

    if "_test" in current_file_path:
      Helper.run_cmd("bundle exec ruby -I test "+ current_file_path)
    else:
      sublime.status_message("iTerm Execute: Current file is not a test file.")
