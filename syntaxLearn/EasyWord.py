#-*_coding:utf-8_*_
import win32com.client

class EasyWord:
    def __init__(self,filename=None):
        print 'init'
        
        self.app=win32com.client.Dispatch("wps.Application")
        print 'init2'
        self.app.Visible=False
        if filename:
            self.doc=self.app.Documents.Open(filename)
    def read(self):
        wrange=self.doc.Range(1,2)#(self.doc.Content.Start,self.doc.Content.End)
        print wrange
        paras=self.doc.Paragraphs.Count
        print paras
        print self.doc.Paragraphs(1).Text
    def readTable(self):
        tableNums=self.doc.Tables.Count;
        print tableNums
    
    def saveAsHtml(self,filename):
        self.doc.SaveAs(filename,8);
        self.doc.Close()
        self.app.Quit()
print 'Easyword'
if True:#__name__=="__main__":
    print 'main'
    file='E:/IWantToBigSmall.docx'
    print 'hello'
    file2='E:\\我要变强测试用例 - 副本.docx'
    print 'hello2'
    word=EasyWord(file)
    print 'hello3'
    #word.readTable()
    #word.read()
    word.saveAsHtml("F:\\table5.html")
    print 'end'
 
        