library(ggplot2)

df <- read.csv("datos_admisiones.csv", header= T)


# sesgos en el numero de aplicaciones
theme_set(theme_light())
g <- ggplot(df, aes(x = Sexo, fill=Sexo)) + 
  facet_wrap(~Facultad.a.la.que.aplicó) + 
  labs(title= "Sesgos en el numero de aplicacion por facultad",
       ylabel= "# aplicaciones x facu")+
  geom_bar(stat = "count")
g

# sesgos en la aceptacion de aplicaciones
df_admitidos <- df[df$Fue.admitido == "S", ]

g <- ggplot(df_admitidos, aes(x = Sexo, fill=Sexo)) + 
  facet_wrap(~Facultad.a.la.que.aplicó) + 
  labs(title= "Sesgos en la aceptacion de la aplicacion",
       ylabel= " aceptados x facu")+
  geom_bar(stat = "count")
g

# sesgos en el rechazo de aplicaciones
df_rechazados <- df[df$Fue.admitido == "N", ]

g <- ggplot(df_rechazados, aes(x = Sexo, fill=Sexo)) + 
  facet_wrap(~Facultad.a.la.que.aplicó) + 
  geom_bar(stat = "count")+
  labs(title= "Sesgos en el rechazo de la aplicacion")

g







