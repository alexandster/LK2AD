#read max_cluster_scales file
scales <- read.table("aSTKDE.txt", sep = ",", dec = ".")

newscales <- scales[ which(scales$V1>0 & scales$V2 > 0 & scales$V3 > 0), ]

#--------------------------------------------------------------------
library(plotly)
inTable <- table(newscales$V5,newscales$V6)

a <- list(
  autotick = TRUE,
  showline = TRUE,
  ticks = "outside",
  tick0 = 0,
  dtick = 0.25,
  ticklen = 5,
  tickwidth = 2,
  tickcolor = toRGB("black")
)

ax <- list(
  zeroline = TRUE,
  showline = TRUE,
  mirror = "ticks",
  gridcolor = toRGB("gray50"),
  gridwidth = 2,
  zerolinecolor = toRGB("red"),
  zerolinewidth = 4,
  linecolor = toRGB("black"),
  linewidth = 6
)

minSBw <- [...]	#minimum spatial bandwidth
maxSBw <- [...]	#maximum spatial bandwidth
SInt <- [...]	#spatial bandwidth step
minTBw <- [...]	#minimum temporal bandwidth
maxTBw <- [...]	#minimum temporal bandwidth
TInt <- [...] #spatial bandwidth step

p <- plot_ly(
  x = seq(minSBw, maxSBw, SInt),
  y = seq(minTBw, maxTBw, TInt),
  z = log(inTable,2),
  type = "contour") %>%
  layout(xaxis = a, yaxis = a)


Sys.setenv("plotly_username"="[your username]")
Sys.setenv("plotly_api_key"="[your api key]")


chart_link = api_create(p, filename="mulitple-trace")
chart_link
#--------------------------------------------------------------------
