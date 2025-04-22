#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <chrono>
#include <thread>
#include <random>
#include <ctime>  // for time and localtime

int main() {
    int count = 0;
    char label[5][10] = {"boat", "dolphin", "fish", "whale", "none"};
    srand( time(NULL) );
    double i;
    int t;
    while (true) {
        // Get current time as time_t
        std::time_t now = std::time(nullptr);
        // Convert to local time string
        char timeStr[100];
        std::strftime(timeStr, sizeof(timeStr), "%Y-%m-%d %H:%M:%S", std::localtime(&now));

        // Output
        std::cout << "Line " << count++ << std::endl;
        std::cout << "Time " << timeStr << std::endl;
        i = ((double) rand() / (RAND_MAX));
        t = rand();
        std::cout << "output result : [" << std::fixed << std::setprecision(6) << float(i) << ", " <<  float(i) << ", " <<  float(i) << ", " <<  float(i) << ", ]" << std::endl;
        std::cout << "\033[35mThe prediction is " << label[t%5] << " " << timeStr << "\033[0m." << std::endl;
        
        std::this_thread::sleep_for(std::chrono::seconds(3));

        std::cout << "Line " << count++ << std::endl;
        std::cout << "Time " << timeStr << std::endl;
        i = ((double) rand() / (RAND_MAX));
        t = rand();
        std::cout << "output result : [" << std::fixed << std::setprecision(6) << float(i) << ", " <<  float(i) << ", " <<  float(i) << ", " <<  float(i) << ", ]" << std::endl;
        std::cout << "\033[35mThe prediction is " << label[t%5] << " + " << label[(t+1)%5] << " " << timeStr << "\033[0m." << std::endl;
        
        std::this_thread::sleep_for(std::chrono::seconds(3));

        std::cout << "Line " << count++ << std::endl;
        std::cout << "Time " << timeStr << std::endl;
        i = ((double) rand() / (RAND_MAX));
        t = rand();
        std::cout << "output result : [" << std::fixed << std::setprecision(6) << float(i) << ", " <<  float(i) << ", " <<  float(i) << ", " <<  float(i) << ", ]" << std::endl;
        std::cout << "\033[35mThe prediction is " << label[t%5] << " + " << label[(t+1)%5] << " + " << label[(t+2)%5]<< " " << timeStr << "\033[0m." << std::endl;
        
        std::this_thread::sleep_for(std::chrono::seconds(3));

        std::cout << "Line " << count++ << std::endl;
        std::cout << "Time " << timeStr << std::endl;
        i = ((double) rand() / (RAND_MAX));
        t = rand();
        std::cout << "output result : [" << std::fixed << std::setprecision(6) << float(i) << ", " <<  float(i) << ", " <<  float(i) << ", " <<  float(i) << ", ]" << std::endl;
        std::cout << "\033[35mThe prediction is " << label[t%5] << " + " << label[(t+1)%5] << " + " << label[(t+2)%5] << " + " << label[(t+3)%5] << " " << timeStr << "\033[0m." << std::endl;
        
        std::this_thread::sleep_for(std::chrono::seconds(3));
    }
}
