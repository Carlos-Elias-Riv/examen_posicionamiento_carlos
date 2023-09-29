library(ggplot2)

df <- read.csv("datos_admisiones.csv", header= T)
# cuantos aplican a la escuela
theme_set(theme_light())
g <- ggplot(df, aes(x = Sexo, fill=Sexo)) +
  labs(title= "Cuantos aplican a la escuela")+
  geom_bar(stat = "count")
g

# sesgos en el numero de aplicaciones

g <- ggplot(df, aes(x = Sexo, fill=Sexo)) + 
  facet_wrap(~Facultad.a.la.que.aplicó) + 
  labs(title= "Cuantos aplican por facultad",
       subtitle = "Por facultad")+
  geom_bar(stat = "count")
g

# sesgos en la aceptacion de aplicaciones
df_admitidos <- df[df$Fue.admitido == "S", ]

g <- ggplot(df_admitidos, aes(x = Sexo, fill=Sexo)) + 
  facet_wrap(~Facultad.a.la.que.aplicó) + 
  labs(title= "Cuantos fueron admitidos de todos los que aplicaron",
       subtitle = "Por facultad")+
  geom_bar(stat = "count")
g

# sesgos en el rechazo de aplicaciones
df_rechazados <- df[df$Fue.admitido == "N", ]

g <- ggplot(df_rechazados, aes(x = Sexo, fill=Sexo)) + 
  facet_wrap(~Facultad.a.la.que.aplicó) + 
  geom_bar(stat = "count")+
  labs(title= "Cuantos fueron rechazados de todos los que aplicaron",
       subtitle= "Por facultad")

g

palet_colors <- c("#77DD77", "#FF6961")
# falta contestar, de todos los que aplicaron (por genero) que porcentaje fue admitido
g <- ggplot(df, aes(x=Sexo)) +
  scale_fill_manual(name= "Admitido", labels = c("Sí", "No"), values = palet_colors)+
  facet_wrap(~Facultad.a.la.que.aplicó) +
  geom_bar(aes(fill=Fue.admitido)) +
  labs(title = "De todos los aplicantes por género que proporción fue admitida",
       subtitle= "Por facultad")
g

g <- ggplot(df, aes(x=Sexo)) +
  scale_fill_manual(name= "Admitido", labels = c("Sí", "No"), values = palet_colors)+
  geom_bar(aes(fill=Fue.admitido)) +
  labs(title = "De todos los aplicantes por género que proporción fue admitida")
g




