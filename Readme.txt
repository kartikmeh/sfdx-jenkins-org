tools required: 

git cli - version 2.24
python - version 3.0 or greater
groovy - 3.0 or grater


pre requisits:
1. set environment variables for all the  tools written above.
2. run "pip install os-system" on cmd.


Steps:

1. copy all files to the source root directory

2. run Git command to find difference between current commit and last successfull commit and save it to list file -
 "git diff-tree --no-commit-id --name-only -r head^ head > list.txt"
 
3. run python script "copyDeltaFiles.py" to copy all different files in delta folder.

4. run groovy script using below command to create the package xml file  -
	"groovy PackageXMLGenerator.groovy delta/force-app/main/default delta/force-app/main/default/package.xml"

5. run sfdx commands below to deploy on salesforce server - 
	"sfdx force:mdapi:deploy -d delta/force-app/main/default -w 30"