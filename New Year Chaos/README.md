statement: https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four

The idea for this problem first arose in the following way: The total number of bribes was given by the sum of the number of elements with smaller values to the right of each person.

However, this solution is O(N^2) which exceeded the time limit for solving the problem. We need to find a solution of 
O(N) order, that is, we need to traverse the queue only once.

So, another way of thinking was necessary. Another important characteristic that could be leveraged from the challenge was that the Nth element of the initial list can only reach up to the position N−2 in the final queue. Otherwise, it has performed more than 2 bribes. Thus, we can analyze the queue from the last element, as the person who should be in position N is either in N−2 or N−1. Therefore, we can perform the "reverse bribe" one or two times to position them where they should be. After that, just look at the queue based on the N−1 element. With this, our solution algorithm only traverses the array once, always looking at the last 3 elements, which makes the complexity order of the problem O(N).