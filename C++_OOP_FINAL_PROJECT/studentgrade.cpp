#include <iostream>
#include <algorithm> 
#include <cstring>   
using namespace std;

// Define the Student structure
struct Student {
    char name[30];   
    int* grades;     
    int nGrades;     
};

// Abstract base class for grade metrics
class GradeMetric {
public:
    virtual float compute(const Student* student) = 0; 
    virtual ~GradeMetric() {} 
};

// Derived class for MedianMetric
class MedianMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        int n = student->nGrades;
        if (n == 0) return 0;

        int* temp = new int[n];  
        for (int i = 0; i < n; ++i)
            *(temp + i) = *(student->grades + i);  

        sort(temp, temp + n);  

        float median;
        if (n % 2 == 0)
            median = (*(temp + n / 2 - 1) + *(temp + n / 2)) / 2.0f;
        else
            median = *(temp + n / 2);

        delete[] temp;
        return median;
    }
};

// Derived class for ModeMetric
class ModeMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        int n = student->nGrades;
        if (n == 0) return 0;

        int mode = *(student->grades);
        int maxCount = 0;

        for (int i = 0; i < n; ++i) {
            int count = 0;
            for (int j = 0; j < n; ++j) {
                if (*(student->grades + j) == *(student->grades + i))
                    count++;
            }
            if (count > maxCount) {
                maxCount = count;
                mode = *(student->grades + i);
            }
        }
        return mode;
    }
};

// Function to add a grade to a student
void addGrade(Student& student, int newGrade) {
    int* newArray = new int[student.nGrades + 1];
    for (int i = 0; i < student.nGrades; ++i) {
        *(newArray + i) = *(student.grades + i);
    }
    *(newArray + student.nGrades) = newGrade;

    delete[] student.grades;
    student.grades = newArray;
    student.nGrades++;
}

// Function to remove a grade by index
void removeGrade(Student& student, int index) {
    if (index < 0 || index >= student.nGrades) return;

    int* newArray = new int[student.nGrades - 1];
    for (int i = 0, j = 0; i < student.nGrades; ++i) {
        if (i != index)
            *(newArray + j++) = *(student.grades + i);
    }

    delete[] student.grades;
    student.grades = newArray;
    student.nGrades--;
}

// MAIN function to demonstrate the system
int main() {
    // Initialize a student
    Student s;
    strcpy(s.name, "John Doe");
    s.grades = nullptr;
    s.nGrades = 0;

    // Add some grades
    addGrade(s, 85);
    addGrade(s, 92);
    addGrade(s, 78);
    addGrade(s, 92);
    addGrade(s, 88);

    // Create metric objects and store in dynamic array
    GradeMetric** metrics = new GradeMetric*[2];
    metrics[0] = new MedianMetric();
    metrics[1] = new ModeMetric();

    // Display grades
    cout << "Student: " << s.name << endl;
    cout << "Grades: ";
    for (int i = 0; i < s.nGrades; ++i) {
        cout << *(s.grades + i) << " ";
    }
    cout << endl;

    // Compute and display metrics
    cout << "Median: " << metrics[0]->compute(&s) << endl;
    cout << "Mode: " << metrics[1]->compute(&s) << endl;

    // Remove a grade (example: index 2)
    removeGrade(s, 2);
    cout << "\nAfter removing grade at index 2:" << endl;
    cout << "Grades: ";
    for (int i = 0; i < s.nGrades; ++i) {
        cout << *(s.grades + i) << " ";
    }
    cout << endl;

    // Recompute metrics
    cout << "New Median: " << metrics[0]->compute(&s) << endl;
    cout << "New Mode: " << metrics[1]->compute(&s) << endl;

    // Cleanup
    delete metrics[0];
    delete metrics[1];
    delete[] metrics;
    delete[] s.grades;

    return 0;
}

