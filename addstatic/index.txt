document.addEventListener("DOMContentLoaded", function () {
  document.forms['classform'].addEventListener('submit', (e) => {
      e.preventDefault();
      a = new URLSearchParams(new FormData(e.target));

      emptyvals = []
      a.forEach((value, key) => {
          if (value == '') {
            emptyvals.push(key);
          }
        });
        
      emptyvals.forEach(key => {
          a.delete(key);
      });
        
      fetch("https://limitless-lake-64230.herokuapp.com/api/?" + a.toString())
      .then((resp) => {
          return resp.json();
      }).then((messagebody) => {
          manipulateDomFromJson(messagebody)
      });
  });
});

function manipulateDomFromJson(jsonobject){
  table = document.getElementById('classoutput');
  htmlstring = "";
  for (section of jsonobject){
      htmlstring += "<tr>"
      for (let attribute in section){
        celltext = ""
        if(attribute === 'tags'){
          for (tag in section['tags']){
            celltext += section['tags'][tag]['tagabbr'] + ", ";
          }
          celltext = celltext.substring(0, celltext.length - 2);
        }
        else{ celltext += section[attribute] }
        htmlstring += "<td>" + celltext + "</td>";
      }
      htmlstring += "</tr>";
  }
  table.innerHTML = htmlstring;
}
