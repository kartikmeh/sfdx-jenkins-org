	def SF_CONSUMER_KEY=env.SF_CONSUMER_KEY
    def SF_USERNAME=env.SF_USERNAME
    def SERVER_KEY_CREDENTIALS_ID=env.SERVER_KEY_CREDENTIALS_ID
	//def DEPLOYDIR='force-app'
    def TEST_LEVEL='RunLocalTests'
    def SF_INSTANCE_URL = env.SF_INSTANCE_URL ?: "https://login.salesforce.com"
    def toolbelt = tool 'toolbelt'
	println SF_CONSUMER_KEY
	println SERVER_KEY_CREDENTIALS_ID


pipeline{
agent any


stages{
	

	stage ('fetch data for deltaDeploy'){
	

		steps{
				bat 'powershell -command "git diff-tree --no-commit-id --name-only -r head^ head > list.txt"'
				bat 'python copyDeltaFiles.py'
				bat 'groovy PackageXMLGenerator.groovy delta/force-app/main/default delta/force-app/main/default/package.xml'

		}
	}
	
	
	stage('Authorize to Salesforce') {
	steps{
	withEnv(["HOME=${env.WORKSPACE}"]) {	
	
	    withCredentials([file(credentialsId: SERVER_KEY_CREDENTIALS_ID, variable: 'server_key_file')]) {
		// -------------------------------------------------------------------------
		// Authenticate to Salesforce using the server key.
		// -------------------------------------------------------------------------

			rc = command "${toolbelt}/sfdx force:auth:jwt:grant --instanceurl ${SF_INSTANCE_URL} --clientid ${SF_CONSUMER_KEY} --jwtkeyfile ${server_key_file} --username ${SF_USERNAME} --setalias vscodeOrg"
		    if (rc != 0) {
			error 'Salesforce org authorization failed.'
		    }
		}
		}
		}
		}
		stage('Deploy and Run Tests') {
		steps{
			rc = command "${toolbelt}/sfdx force:mdapi:deploy -d delta/force-app/main/default -w 30"
		    if (rc != 0) {
			error 'Salesforce deploy and test run failed.'
		    }
		}
		}
}
}
def command(script) {
    if (isUnix()) {
        return sh(returnStatus: true, script: script);
    } else {
		return bat(returnStatus: true, script: script);
    }
}