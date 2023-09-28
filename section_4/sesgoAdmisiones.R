library(ggplot2)

df <- read.csv("datos_admisiones.csv", header= T)

theme_set(theme_light())
g <- ggplot(df, aes(x = Sexo, fill=Sexo)) + 
  facet_wrap(~Facultad.a.la.que.aplicó) + 
  labs(title= "Mostrar sesgos sin discriminar a los que fueron admitidos los que no")+
  geom_bar(stat = "count")
g


df_admitidos <- df[df$Fue.admitido == "S", ]

g <- ggplot(df_admitidos, aes(x = Sexo, fill=Sexo)) + 
  facet_wrap(~Facultad.a.la.que.aplicó) + 
  labs(title= "Sesgos en la aceptacion de la admision")+
  geom_bar(stat = "count")
g

df_rechazados <- df[df$Fue.admitido == "N", ]

g <- ggplot(df_rechazados, aes(x = Sexo, fill=Sexo)) + 
  facet_wrap(~Facultad.a.la.que.aplicó) + 
  labs(title= "Sesgos en el rechazo de la admision")+
  geom_bar(stat = "count")
g