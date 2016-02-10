import sublime, sublime_plugin
from .helper import Helper

class Executer:
  def __init__(self, view):
    self.view = view

  def try_to_execute_current_text(self, text):
    title = Helper.get_test_title(text)

    if title is not None:
      formated_title = Helper.text_to_regex(title)
      current_file_path = Helper.file_name_from_project(self.view.file_name(), Helper.first_project_path())

      Helper.run_cmd("bundle exec ruby -I test "+ current_file_path + " -n /"+ formated_title +"/")

      return True
    else:
      return False

  def try_to_execute_current_file(self, file_name):
    current_file_path = Helper.file_name_from_project(file_name, Helper.first_project_path())

    if "_test" in current_file_path:
      Helper.run_cmd("bundle exec ruby -I test "+ current_file_path)
      return True
    else:
      return False

class ItermExecuteRunCurrentContextCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    current_line = self.view.substr(self.view.line(self.view.sel()[0]))
    executer = Executer(self.view)

    if not executer.try_to_execute_current_text(current_line):
      sublime.status_message("iTerm Execute: No test title on current line.")

class ItermExecuteRunCurrentFileCommand(sublime_plugin.TextCommand, sublime_plugin.WindowCommand):

  def run(self, edit):
    executer = Executer(self.view)

    if not executer.try_to_execute_current_file(self.view.file_name()):
      sublime.status_message("iTerm Execute: Current file is not a test file.")
