var currentQuote = "This is a quote from someone you've never heard of.",
  currentAuthor = "Someone";

var colors = [
  "#6ea500",
  "#00a579",
  "#5000a5",
  "#a5009f",
  "#002aa5",
  "#a5a100",
  "hotpink"
];

function updatePage(quoteObj) {
  //console.log(quoteObj);
  currentAuthor = quoteObj.quoteAuthor == "" ? "Unknown" : quoteObj.quoteAuthor;
  currentQuote = quoteObj.quoteText == "" ? "This is a quote from someone you've never heard of." : quoteObj.quoteText;

  /* change color */
  $("body")
    .get(0)
    .style.setProperty(
      "--page-color",
      colors[Math.floor(Math.random() * colors.length)]
    );

  /* change quote */
  $("#quote").text(currentQuote);

  /* change author */
  $("#author").text("by " + currentAuthor);

  /* change tweet link */
  $("#tweet-quote").attr(
    "href",
    "https://twitter.com/intent/tweet?hashtags=quotes&text=" +
      encodeURIComponent('"' + currentQuote + '" ' + currentAuthor)
  );
}

function getQuote() {
  console.log('getQuote fired');
  $.ajax({
    headers: {
      Accept: "application/json"
    },
    url:
      "https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?",
    type: "GET",
    dataType: "jsonp",
    success: updatePage
  }); //ajax
} //function

$("#new-quote").click(function () {
  getQuote();
  console.log(currentQuote, currentAuthor);
});

//$(getQuote);