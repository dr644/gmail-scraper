var SHEET_ID = "1j77lcrAEoldoJ_0gXupna56uuKsNv1K56-yDN36H2E8";
var SHEET_NAME = "inbox2xls";

function getEmails_(q){
  var emails = [];
  var thds = GmailApp.search(q);
  for(var i in thds){
    var msgs = thds[i].getMessages();
    for(var j in msgs){
      emails.push([msgs[j].getPlainBody().replace(/<.*?>/g, '\n').replace(/^\s*\n/gm, '').replace(/^\s*/gm, '').replace(/\s*\n/gm, '\n')]);
    }
  }
  return emails;
}

function appendData_(sheet, array2d){
    sheet.getRange(sheet.getLastRow() + 1, 1, array2d.length, array2d[0].length).setValues(array2d);
}

function run(){
  //Gmail Advanced search https://support.google.com/mail/answer/7190
  array2d = getEmails_("from:customer_support@email.ticketmaster.com | from:guestservices@boxoffice.axs.com");
  if(array2d) {
    var ss = SpreadsheetApp.openById(SHEET_ID);
    var sheet = ss.getSheetByName(SHEET_NAME);
    if(!sheet) sheet = ss.insertSheet(SHEET_NAME);
    appendData_(sheet, array2d);
  }


}
