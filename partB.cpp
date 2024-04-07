#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>

using namespace cv;
using namespace std;

int main() {
    Mat img = imread("sample_input.jpg");

    // Apply denoising
    fastNlMeansDenoisingColored(img, img, 10, 10, 7, 21);

    // Save denoised image
    imwrite("filtered_noise.png", img);

    int x = img.cols;
    int y = img.rows;
    int black_threshold = 80;
    int blue_threshold = 150;

    vector<int> xs;
    vector<int> ys;
    vector<vector<int>> final;

    // Find black rows
    for (int i = 0; i < y; ++i) {
        Scalar avg = mean(img.row(i));
        if (avg[0] < black_threshold) {
            ys.push_back(i);
            for (int j = 0; j < x; ++j) {
                img.at<Vec3b>(i, j) = Vec3b(0, 0, 0);
            }
        }
    }

    // Find black columns
    for (int i = 0; i < x; ++i) {
        Scalar avg = mean(img.col(i));
        if (avg[0] < black_threshold) {
            xs.push_back(i);
            for (int j = 0; j < y; ++j) {
                img.at<Vec3b>(j, i) = Vec3b(0, 0, 0);
            }
        }
    }

    int columns = xs.size() - 1;
    int rows = ys.size() - 1;

    // Process blocks
    for (int i = 0; i < rows; ++i) {
        vector<int> row_arr;
        for (int j = 0; j < columns; ++j) {
            Scalar avg(0, 0, 0);
            for (int a = ys[i] + 1; a < ys[i + 1]; ++a) {
                for (int b = xs[j] + 1; b < xs[j + 1]; ++b) {
                    avg += img.at<Vec3b>(a, b) / ((ys[i + 1] - ys[i] - 1) * (xs[j + 1] - xs[j] - 1));
                }
            }
            if (avg[0] > blue_threshold)
                row_arr.push_back(1);
            else
                row_arr.push_back(0);

            for (int a = ys[i] + 1; a < ys[i + 1]; ++a) {
                for (int b = xs[j] + 1; b < xs[j + 1]; ++b) {
                    if (row_arr.back() == 1)
                        img.at<Vec3b>(a, b) = Vec3b(255, 0, 0);
                    else
                        img.at<Vec3b>(a, b) = Vec3b(0, 255, 255);
                }
            }
        }
        final.push_back(row_arr);
    }

    // Breadth-First Search to find shortest path

    // Backtracking

    // Draw shortest path

    // Save the result
    imwrite("answer.png", img);

    return 0;
}
