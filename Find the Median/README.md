statement: https://www.hackerrank.com/challenges/find-the-median/problem

For this problem, there's an easy way to solve it by using pre-built functions to sort the array, and after sorthing you can either take the middle numbler, in case len(arr) odd, or the average of the two middle ones, if len(arr) even.

I implemented that idea in both Pyhton and C++.

In Python I used the  V = sorted(arr) function, and in C++ I used std::sort(v.begin(), v.end()), with v being a std::vector<int>.

The other way to solve it, whithout using sorting functions, is by finding the i-st smallest element in your arr. In fact, you just need to find the n/2 and the n/2 - 1 smallest elements.



