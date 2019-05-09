install.packages(c("cluster", "factoextra", "clValid"))
library(data.table)
library(cluster)
library(factoextra)
library(clValid) #validation

# combine graph names to one list
combineListsAsOne <-function(list1, list2){
  n <- c()
  for(x in list1){
    n<-c(n, x)
  }
  for(y in list2){
    n<-c(n, y)
  }
  return(n)
}

#ids für die graphen setzen
setids <- function(integer) {
  n <- matrix(c(integer), dimnames = list(graphs))
  return(n)
}

#graphs numbered
graphs <- combineListsAsOne(list(0:86), NULL)

### data ###
min_symmetrized <- fread("min_symmetrized_matrix_lenz.csv", header=FALSE, sep=";", quote="\"", strip.white=TRUE, showProgress=TRUE, encoding="UTF-8", na.strings=c("", "null"), stringsAsFactors=FALSE)
max_symmetrized <- fread("max_symmetrized_matrix_lenz.csv", header=FALSE, sep=";", quote="\"", strip.white=TRUE, showProgress=TRUE, encoding="UTF-8", na.strings=c("", "null"), stringsAsFactors=FALSE)
avg_symmetrized <- fread("avg_symmetrized_matrix_lenz.csv", header=FALSE, sep=";", quote="\"", strip.white=TRUE, showProgress=TRUE, encoding="UTF-8", na.strings=c("", "null"), stringsAsFactors=FALSE)
vectors <- fread("vectors_lenz.txt", header=FALSE, sep=";", quote="\"", strip.white=TRUE, showProgress=TRUE, encoding="UTF-8", na.strings=c("", "null"), stringsAsFactors=FALSE)

min_matrix <- matrix(c(min_matrix), nr = 87, dimnames = list(graphs))
max_matrix <- matrix(c(max_matrix), nr = 87, dimnames = list(graphs))
avg_matrix <- matrix(c(avg_matrix), nr = 87, dimnames = list(graphs))
vectors_matrix <- as.matrix(vectors)
############

######### min
### k-medoid
fviz_nbclust(min_symmetrized, pam, k.max = 18)
intern <- clValid(min_matrix, 2, clMethods=c("pam"),
                  validation="internal")
summary(intern)
# k = Anzahl Themen
c <- eclust(min_symmetrized, k = 18, "pam", graph = FALSE)
index <- setids(c$clustering)
index
#
###
### agnes
# single
fviz_nbclust(min_symmetrized, hcut, k.max = 18, hc_method = "single")
intern <- clValid(min_matrix, 2, clMethods=c("agnes"),
                  validation="internal", method = "single")
summary(intern)
c <- eclust(min_symmetrized, k = 18, "agnes", graph = FALSE, hc_method = "single")
index <- setids(c$cluster)
index
#
# complete
fviz_nbclust(min_symmetrized, hcut, k.max = 18, hc_method = "complete")
intern <- clValid(min_matrix, 4, clMethods=c("agnes"),
                  validation="internal", method = "complete")
summary(intern)
c <- eclust(min_symmetrized, k = 18, "agnes", graph = FALSE, hc_method = "complete")
index <- setids(c$cluster)
index
#
# average
fviz_nbclust(min_symmetrized, hcut, k.max = 18, hc_method = "average")
intern <- clValid(min_matrix, 2, clMethods=c("agnes"),
                  validation="internal", method = "average")
summary(intern)
c <- eclust(min_symmetrized, k = 18, "agnes", graph = FALSE, hc_method = "average")
index <- setids(c$cluster)
index
#
# ward
fviz_nbclust(min_symmetrized, hcut, k.max = 18, hc_method = "ward.D2")
intern <- clValid(min_matrix, 2, clMethods=c("agnes"),
                  validation="internal", method = "ward")
summary(intern)
c <- eclust(min_symmetrized, k = 5, "agnes", graph = FALSE, hc_method = "ward")
index <- setids(c$cluster)
index
#
#########

######### max
### k-medoid
fviz_nbclust(max_symmetrized, pam, k.max = 18)
intern <- clValid(max_matrix, 2, clMethods=c("pam"),
                  validation="internal")
summary(intern)
# k = Anzahl Themen
c <- eclust(max_matrix, k = 18, "pam", graph = FALSE)
index <- setids(c$clustering)
index
#
###
#agnes
# single
fviz_nbclust(max_symmetrized, hcut, k.max = 18, hc_method = "single")
intern <- clValid(max_matrix, 2, clMethods=c("agnes"),
                  validation="internal", method = "single")
summary(intern)
c <- eclust(max_symmetrized, k = 5, "agnes", graph = FALSE, hc_method = "single")
index <- setids(c$cluster)
index
# 
# complete
fviz_nbclust(max_symmetrized, hcut, k.max = 18, hc_method = "complete")
intern <- clValid(max_matrix, 2, clMethods=c("agnes"),
                  validation="internal", method = "complete")
summary(intern)
c <- eclust(max_symmetrized, k = 18, "agnes", graph = FALSE, hc_method = "complete")
index <- setids(c$cluster)
index
#
# average
fviz_nbclust(max_symmetrized, hcut, k.max = 18, hc_method = "average")
intern <- clValid(max_matrix, 2, clMethods=c("agnes"),
                  validation="internal", method = "average")
summary(intern)
c <- eclust(max_symmetrized, k = 18, "agnes", graph = FALSE, hc_method = "average")
index <- setids(c$cluster)
index
#
# ward
fviz_nbclust(max_symmetrized, hcut, k.max = 18, hc_method = "ward.D2")
intern <- clValid(max_matrix, 3, clMethods=c("agnes"),
                  validation="internal", method = "ward")
summary(intern)
c <- eclust(max_symmetrized, k = 18, "agnes", graph = FALSE, hc_method = "ward")
index <- setids(c$cluster)
index
#
#########

######### avg
### k-medoid
fviz_nbclust(avg_symmetrized, pam, k.max = 18)
intern <- clValid(avg_matrix, 2, clMethods=c("pam"),
                  validation="internal")
summary(intern)
# k = Anzahl Themen
c <- eclust(avg_symmetrized, k = 18, "pam", graph = FALSE)
index <- setids(c$clustering)
index
#
### agnes
# single
fviz_nbclust(avg_symmetrized, hcut, k.max = 18, hc_method = "single")
intern <- clValid(avg_matrix, 2, clMethods=c("agnes"),
                  validation="internal", method = "single")
summary(intern)
c <- eclust(avg_symmetrized, k = 5, "agnes", graph = FALSE, hc_method = "single")
index <- setids(c$cluster)
index
#
# complete
fviz_nbclust(avg_symmetrized, hcut, k.max = 18, hc_method = "complete")
intern <- clValid(avg_matrix, 3, clMethods=c("agnes"),
                  validation="internal", method = "complete")
summary(intern)
c <- eclust(avg_symmetrized, k = 18, "agnes", graph = FALSE, hc_method = "complete")
index <- setids(c$cluster)
index
#
# average
fviz_nbclust(avg_symmetrized, hcut, k.max = 18, hc_method = "average")
intern <- clValid(avg_matrix, 3, clMethods=c("agnes"),
                  validation="internal", method = "average")
summary(intern)
c <- eclust(avg_symmetrized, k = 18, "agnes", graph = FALSE, hc_method = "average")
index <- setids(c$cluster)
index
#
# ward
fviz_nbclust(avg_symmetrized, hcut, k.max = 18, hc_method = "ward.D2")
intern <- clValid(avg_matrix, 2, clMethods=c("agnes"),
                  validation="internal", method = "ward")
summary(intern)
c <- eclust(avg_symmetrized, k = 18, "agnes", graph = FALSE, hc_method = "ward")
index <- setids(c$cluster)
index
#
#########

######### Vectors
### k-medoid
fviz_nbclust(vectors, pam, k.max = 18)
intern <- clValid(vectors_matrix, 18, clMethods=c("pam"),
                  validation="internal")
summary(intern)
# k = Anzahl Themen
c <- eclust(vectors, k = 5, "pam", graph = FALSE)
index <- setids(c$clustering)
index
#
### agnes
# single
fviz_nbclust(vectors, hcut, k.max = 18, hc_method = "single")
intern <- clValid(vectors_matrix, 2, clMethods=c("agnes"),
                  validation="internal", method = "single")
summary(intern)
c <- eclust(vectors, k = 5, "agnes", graph = FALSE, hc_method = "single")
index <- setids(c$cluster)
index
#
# complete
fviz_nbclust(vectors, hcut, k.max = 18, hc_method = "complete")
intern <- clValid(vectors_matrix, 16, clMethods=c("agnes"),
                  validation="internal", method = "complete")
summary(intern)
c <- eclust(vectors, k = 18, "agnes", graph = FALSE, hc_method = "complete")
index <- setids(c$cluster)
index
#
# average
fviz_nbclust(vectors, hcut, k.max = 18, hc_method = "average")
intern <- clValid(vectors_matrix, 2, clMethods=c("agnes"),
                  validation="internal", method = "average")
summary(intern)
c <- eclust(vectors, k = 18, "agnes", graph = FALSE, hc_method = "average")
index <- setids(c$cluster)
index
#
# ward
fviz_nbclust(vectors, hcut, k.max = 18, hc_method = "ward.D2")
intern <- clValid(vectors_matrix, 5, clMethods=c("agnes"),
                  validation="internal", method = "ward")
summary(intern)
c <- eclust(vectors, k = 18, "agnes", graph = FALSE, hc_method = "ward")
index <- setids(c$cluster)
index
#
#########

########## Tests

clusters <- c(2:18)
for(current in clusters){
  c <- eclust(vectors, k = current, "agnes", graph = FALSE, hc_method = "complete")
  print(paste(current, c$silinfo$avg.width, c$id.med))
}


vec_medoid <- eclust(vectors, k = 5, "pam", graph = FALSE)
vec_medoid <- pam(vectors, 5)
fviz_cluster(vec_medoid)
vec_medoid$silinfo
vm <- setids(vec_medoid$cluster)
vm

vec_agnes <- eclust(vectors, k = 18, "agnes", graph = FALSE, hc_method = "single")
install.packages('igraph')
fviz_dend(vec_agnes, type = "phylogenic")

##########