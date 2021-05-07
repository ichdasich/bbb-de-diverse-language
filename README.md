# bbb-de-diverse-language

This is a rework of the BigBlueButton German translations to follow best practices
for inclusive language. Changes are in `de_changes.json`. You can apply them to 
the upstream version of BBB with the following steps (you need python3 installed):

```
# Clone repo
git clone https://github.com/ichdasich/bbb-de-diverse-language
cd bbb-de-diverse-language

# Make script executable:
chmod +x ./update_json.py

# create new json file
# Usage: ./update_json.py [changes_file] [input_file] [output_file]
./update_json.py ./de_changes.json /usr/share/meteor/bundle/programs/web.browser/app/locales/de.json ./de_new.json
cat ./de_new.json > /usr/share/meteor/bundle/programs/web.browser/app/locales/de.json
```

A restart of BBB is not necessary for the change to take effect, but the change 
will have to be reapplied upon updates until https://github.com/bigbluebutton/bigbluebutton/issues/12294 
has been resolved.
