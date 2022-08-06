#Nesting a list in dictionary 
travel_log ={
  "France": ["Paris","Lille","Dijon"],
  "Germany": ["Berlin","Hamburg","Stuttgart"]
}

#Nesting Dictionary in a Dictionary
travel_log ={
  "France": {"Cities_visited":["Paris","Lille","Dijon"], "Total_visits":10},
  "Germany": {"Cities_visited":["Berlin","Hamburg","Stuttgart"],"Total_visits":5}
}

#Nesting a Dictionary in a List
travel_log =[
  {
    "Country":"France",
    "Cities_visited":["Paris","Lille","Dijon"],
    "Total_visits":10
  },
  {
    "Country":"Germany",
    "Cities_visited":["Berlin","Hamburg","Stuttgart"],
    "Total_visits":5
  }
]