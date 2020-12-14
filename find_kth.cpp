#include <bits/stdc++.h>
using namespace std;

int findKthsmallest(vector<int> const &v, int k) {
    priority_queue<int, vector<int>> pq(v.begin(), v.begin() + k);
    for (int i=k; i < v.size(); i++) {
        if (v[i] < pq.top()) {
            pq.pop();
            pq.push(v[i]);
        }
    }
    return pq.top();
}

int main() {
    vector<int> vec = {7, 4, 6, 3, 9, 1};
    const size_t k = 3;
    cout << "kth smallest element in an array is " <<
            findKthsmallest(vec, k);
    return 0;
}
