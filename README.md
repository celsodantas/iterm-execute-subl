## iTerm Execute for Sublime

Allows to execute Ruby test in iTerm based on the current Ruby test file or file context. You must have iTerm open and in your project directory.

This project is useful if you are running Vagrant (SSH) and Sublime from your host.

### Execute current file

`ctrl+alt+r` will send the command `bundle exec ruby -I test path_to_test.rb` to iTerm.

### Execute current scope

The cursor must be in the test title. `ctrl+alt+super+r` to execute.

The plugin will extract the test file and send the command to iTerm:

`bundle exec ruby -I test path_to_test.rb -n /title_of_the_test/`

It will parse the test title if you using RSpec format of test:

```ruby
test "title of the test" do
   ...
end
```

It will convert `title of the test` to `title_of_the_test`.

## Installation


Manual installation:

```
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
git clone git@github.com:celsodantas/iterm-execute-subl.git ItermExecute
```
