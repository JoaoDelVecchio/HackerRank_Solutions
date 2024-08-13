[text](https://www.hackerrank.com/challenges/count-triplets-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps)


A ideia principal é criar dois dicionários, numeros que podem ser terceiros e números que podem ser segundos de um triplete.
Ao se percorrer um vetor, verifique se o numéro da casa está em um desses dois dicionários.
Interessante perceber que, uma vez que queremos percorrer o vetor uma única vez, garantindo complexidade temporal O(n), devemos "olhar para o passado" e não se preocupar com o "futuro". Ter isso em mente pode ajudar nas próximas vezes que estiver resolvendo um problema parecido.