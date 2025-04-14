#include <iostream>
#include <chrono>
#include <thread>
#include <ctime>  // for time and localtime
int main() {
    int i = 0;
    while (true) {
        // Get current time as time_t
        std::time_t now = std::time(nullptr);

        // Convert to local time string
        char timeStr[100];
        std::strftime(timeStr, sizeof(timeStr), "%Y-%m-%d %H:%M:%S", std::localtime(&now));

        // Output
        std::cout << "Line " << i++ << std::endl;
        std::cout << "Time " << timeStr << std::endl;
        std::cout << "\033[35mThe prediction is " << i << " " << timeStr << "\033[0m." << std::endl;
        
        std::this_thread::sleep_for(std::chrono::seconds(3));
    }
}
