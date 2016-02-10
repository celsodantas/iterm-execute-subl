import re
import subprocess
import sublime, sublime_plugin

class Helper:
  @classmethod
  def get_test_title(cls, title):
    print(re.search('test .+ do', title))
    if re.findall('test .+ do', title) != None:
      m = re.search('[\'|"](.+)[\'|"]', title)

      if m:
        return m.group(1)
      else:
        return None
    else:
      return None

  @classmethod
  def turn_text_to_regex(cls, text):
    return text.replace(" ", "_")

  @classmethod
  def file_name_from_project(cls, file_path, project_path):
    return file_path.replace(project_path + "/", "")

  @classmethod
  def first_project_path(cls):
    return sublime.active_window().folders()[0]

  @classmethod
  def run_cmd(cls, cmd):
    cmd = cls._clean_cmd(cmd)
    cmd = cls._escape_dquote(cmd)

    script = '''
       tell application "iTerm"
         tell the current terminal
           activate current session
           tell the current session
             write text "code"
           end tell
         end tell
       end tell
    '''

    script = script.replace("code", cmd)

    args = ['osascript']
    args.extend(['-e', script])

    subprocess.Popen(args)

  @classmethod
  def _run_ruby_test_for_file(cls, test_path):
    cls.run_cmd("bundle exec ruby -I test "+ test_path)

  @classmethod
  def _clean_cmd(cls, cmd):
      cmd = cmd.expandtabs(4)
      cmd = cmd.rstrip('\n')
      if len(re.findall("\n", cmd)) == 0:
          cmd = cmd.lstrip()
      return cmd

  @classmethod
  def _escape_dquote(cls, cmd):
      cmd = cmd.replace('\\', '\\\\')
      cmd = cmd.replace('"', '\\"')
      return cmd
