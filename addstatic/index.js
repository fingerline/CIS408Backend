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
            console.log(messagebody)
        });
    });
  });
