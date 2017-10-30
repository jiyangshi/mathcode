/* Use DP(Danymic Programming) to solve
 * Maximum path sum problem
 */
#include <fstream>
// #include <regex>
// #include <string>
#include <vector>
#include <iostream>
using namespace std;

int main()
{
    // First, read all the data in one line, named line
    // Second, do somethings on that data -> matrix
    ifstream fin("triangle.txt");     // Read the file
    vector<int> line;
    int idata;
    while (fin) {
        fin >> idata;
        line.push_back(idata);
    }
    fin.close();                      //  Close the file

    // Change the line to matrix
    vector<int> temp_line;
    vector<vector<int> > matrix;
    for (int i = 1; i <= 100; i++) {
        for (int j = 0; j < i; j++)
            temp_line.push_back(line[(i*(i-1)/2)+j]);
        matrix.push_back(temp_line);
        temp_line.clear();
    }


    // Using DP algorithm to handle maximum path sum
    int res[100][100];
    for (int i = 100; i > 0; --i) {
        for (int j = 0; j < i; ++j) {
            if (i == 100)
                res[i-1][j] = matrix[i-1][j];
            else if (res[i][j] >= res[i][j+1])
                res[i-1][j] = res[i][j] + matrix[i-1][j];
            else
                res[i-1][j] = res[i][j+1] + matrix[i-1][j];
        }
    }

    cout << res[0][0] << endl;

    return 0;
}
