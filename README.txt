Audrey Demo
-----------

This addon can be used to create your own addon once you've created your own JSON file.

1. Edit the file addon.xml, change the following lines;
    Line 2 - <addon id="plugin.video.audreydemo" name="Audrey Demo" version="1.0" provider-name="ptom">
        Replace the id, name, version and provider-name, to those relevant to you and your addon
    Line 11 - <summary lang="en">Demo Addon showing how to use the Audrey script addon.</summary>
        Add your own description for yor addon
2. Comment out the appropraite lines in default.py
3. Rename the containing folder to that of your addon id (the amend in Step 1 Line 2)
4. Zip up the folder and done