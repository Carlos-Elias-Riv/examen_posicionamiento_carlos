library(ggplot2)

df <- read.csv("datos_admisiones.csv", header= T)
# cuantos aplican a la escuela
theme_set(theme_light())
g <- ggplot(df, aes(x = Sexo, fill=Sexo)) +
  labs(title= "Cuantos aplican a la escuela")+
  geom_bar(stat = "count")
g

# length(which(df$Sexo == 'H'))
# length(which(df$Sexo == 'M'))
## hombres:2651 mujeres: 1835
## porcentual 59%, 41%


# sesgos en el numero de aplicaciones

g <- ggplot(df, aes(x = Sexo, fill=Sexo)) + 
  facet_wrap(~Facultad.a.la.que.aplicó) + 
  labs(title= "Cuantos aplican por facultad",
       subtitle = "Por facultad")+
  geom_bar(stat = "count")
g

facus <- c('A', 'B', 'C', 'D', 'E')
sexo <- c("M", "H")

# facus <- c('A', 'B', 'C', 'D', 'E')
# sexo <- c("M", "H")
# 
# for (fac in facus){
#   for (s in sexo){
#     print(paste(fac, s, length(which(df$Sexo == s & df$Facultad.a.la.que.aplicó == fac))))
#   }
# }
# A M 108" porcentaje de mujeres que aplicaron a A: 11%
# A H 825" porcentaje de hombres que aplicaron a A: 89%
# B M 25"  porcentaje de mujeres que aplicaron a B: 4%
# B H 520" porcentaje de hombres que aplicaron a B: 96%
# C M 593" porcentaje de mujeres que aplicaron a C: 64%
# C H 325" porcentaje de hombres que aplicaron a C: 36%
# D M 375" porcentaje de mujeres que aplicaron a D: 47%
# D H 417" porcentaje de hombres que aplicaron a D: 53%
# E M 393" porcentaje de mujeres que aplicaron a E: 67%
# E H 191" porcentaje de hombres que aplicaron a E: 33%





# sesgos en la aceptacion de aplicaciones
df_admitidos <- df[df$Fue.admitido == "S", ]

g <- ggplot(df_admitidos, aes(x = Sexo, fill=Sexo)) + 
  facet_wrap(~Facultad.a.la.que.aplicó) + 
  labs(title= "Cuantos fueron admitidos de todos los que aplicaron",
       subtitle = "Por facultad")+
  geom_bar(stat = "count")
g

## porcentajes de admision por genero

# facus <- c('A', 'B', 'C', 'D', 'E')
# sexo <- c("M", "H")
# 
# for (fac in facus){
#   for (s in sexo){
#     print(paste(fac, s, length(which(df$Sexo == s & df$Facultad.a.la.que.aplicó == fac & df$Fue.admitido == "S"))))
#   }
# }
# A M 89" porcentaje de aceptacion de mujeres que aplicaron a A: 82%
# A H 512" porcentaje de aceptacion de hombres que aplicaron a A: 62%
# B M 17"  porcentaje de aceptacion de mujeres que aplicaron a B: 68%
# B H 313" porcentaje de aceptacion de hombres que aplicaron a B: 60%
# C M 202" porcentaje de aceptacion de mujeres que aplicaron a C: 34%
# C H 120" porcentaje de aceptacion de hombres que aplicaron a C: 37%
# D M 131" porcentaje de aceptacion de mujeres que aplicaron a D: 35%
# D H 138" porcentaje de aceptacion de hombres que aplicaron a D: 33%
# E M 94" porcentaje de aceptacion de mujeres que aplicaron a E: 24%
# E H 53" porcentaje de aceptacion de hombres que aplicaron a E: 28%

# sesgos en el rechazo de aplicaciones
df_rechazados <- df[df$Fue.admitido == "N", ]

g <- ggplot(df_rechazados, aes(x = Sexo, fill=Sexo)) + 
  facet_wrap(~Facultad.a.la.que.aplicó) + 
  geom_bar(stat = "count")+
  labs(title= "Cuantos fueron rechazados de todos los que aplicaron",
       subtitle= "Por facultad")

g

# A M 89" porcentaje de rechazo de mujeres que aplicaron a A: 18%
# A H 512" porcentaje de rechazo de hombres que aplicaron a A: 38%
# B M 17"  porcentaje de rechazo de mujeres que aplicaron a B: 32%
# B H 313" porcentaje de rechazo de hombres que aplicaron a B: 40%
# C M 202" porcentaje de rechazo de mujeres que aplicaron a C: 66%
# C H 120" porcentaje de rechazo de hombres que aplicaron a C: 63%
# D M 131" porcentaje de rechazo de mujeres que aplicaron a D: 65%
# D H 138" porcentaje de rechazo de hombres que aplicaron a D: 67%
# E M 94" porcentaje de rechazo de mujeres que aplicaron a E: 76%
# E H 53" porcentaje de rechazo de hombres que aplicaron a E: 72%

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




