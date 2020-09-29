import groovy.io.FileType

def list = []

def dir = new File("C:\\Users\\kartik\\Desktop\\Salesforce\\Kartik\\sfdx-jenkins-org\\deltaDestruction")
dir.eachFileRecurse (FileType.FILES) { file ->
  list << file
}
String path
String fileWithExtention
String fileWithOutExtention
list.each {
  path=it.path.toString()
  fileWithExtention= path.substring(path.lastIndexOf("\\")+1)
  fileWithOutExtention=fileWithExtention.substring(0,fileWithExtention.lastIndexOf("."))
  println fileWithOutExtention
}
//