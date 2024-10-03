### Comprehensive C++ Programming Language Documentation

C++ is a powerful, high-performance programming language that supports multiple paradigms such as procedural, object-oriented, and generic programming. Initially developed by **Bjarne Stroustrup** in 1979, C++ is an extension of the C programming language with added features like classes and objects.

This documentation covers the **fundamentals of C++**, its **key features**, popular **libraries**, and best **practices**. C++ is widely used in systems programming, game development, real-time systems, and large-scale applications.

---

## Table of Contents

1. [Introduction to C++](#introduction-to-c++)
2. [Basic Structure of a C++ Program](#basic-structure-of-a-c-program)
3. [Variables, Data Types, and Operators](#variables-data-types-and-operators)
4. [Control Flow Statements](#control-flow-statements)
5. [Functions](#functions)
6. [Object-Oriented Programming in C++](#object-oriented-programming-in-c)
7. [Memory Management](#memory-management)
8. [Templates and Generic Programming](#templates-and-generic-programming)
9. [C++ Standard Libraries](#c-standard-libraries)
10. [Best Practices](#best-practices)
11. [Learning Resources](#learning-resources)

---

## 1. Introduction to C++

C++ is a statically-typed, compiled language with low-level memory control and a variety of high-level features. It is known for its **speed**, **efficiency**, and **flexibility**. C++ compilers produce highly optimized machine code, making C++ ideal for performance-critical applications like operating systems, embedded systems, and real-time applications.

### Key Features:
- **Multi-paradigm support**: Supports procedural, object-oriented, and generic programming.
- **Low-level memory manipulation**: Direct control over hardware resources (pointers, manual memory management).
- **Object-Oriented Programming (OOP)**: Supports classes, inheritance, polymorphism, encapsulation, and abstraction.
- **Templates**: Enables generic programming with type-safe functions and classes.
- **Standard Template Library (STL)**: A rich set of algorithms, containers, and iterators.

---

## 2. Basic Structure of a C++ Program

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;  // Print message to console
    return 0;  // Indicate successful program termination
}
```

### Explanation:
- `#include <iostream>`: Preprocessor directive to include standard input/output stream.
- `int main()`: The starting point of every C++ program.
- `std::cout`: Standard output stream (used for printing to the console).
- `return 0`: Return status to the operating system, indicating the program executed successfully.

---

## 3. Variables, Data Types, and Operators

### Variables:
Variables store data of various types. Each variable must have a **type** and a **name**.

```cpp
int age = 30;
float weight = 72.5;
char grade = 'A';
```

### Common Data Types:
- **int**: Integer (whole numbers) – `int a = 10;`
- **float**: Floating-point (single precision) – `float b = 3.14f;`
- **double**: Double precision floating-point – `double c = 2.71828;`
- **char**: Character – `char d = 'Z';`
- **bool**: Boolean – `bool e = true;`

### Operators:
- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `%` (modulus)
- **Relational Operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical Operators**: `&&`, `||`, `!`
- **Assignment Operators**: `=`, `+=`, `-=`, `*=`, `/=`
- **Bitwise Operators**: `&`, `|`, `^`, `~`, `<<`, `>>`

---

## 4. Control Flow Statements

C++ provides various control flow mechanisms for conditional execution and looping.

### Conditional Statements:
- **if/else**:

```cpp
if (condition) {
    // Code block if condition is true
} else {
    // Code block if condition is false
}
```

- **switch/case**:

```cpp
switch (variable) {
    case 1:
        // Code block for case 1
        break;
    case 2:
        // Code block for case 2
        break;
    default:
        // Default code block
        break;
}
```

### Looping Constructs:
- **for loop**:

```cpp
for (int i = 0; i < 10; i++) {
    // Code block
}
```

- **while loop**:

```cpp
while (condition) {
    // Code block
}
```

- **do-while loop**:

```cpp
do {
    // Code block
} while (condition);
```

---

## 5. Functions

Functions are blocks of code designed to perform specific tasks. In C++, functions can be **declared** and **defined**.

```cpp
int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(5, 3);  // Call the add function
    std::cout << result << std::endl;  // Outputs 8
    return 0;
}
```

- **Pass by Value**: Arguments are passed by value, meaning copies are made.
- **Pass by Reference**: Allows functions to modify the original variables using reference parameters (`&`).

---

## 6. Object-Oriented Programming in C++

C++ supports **object-oriented programming (OOP)** which is based on the concepts of **classes** and **objects**.

### Classes and Objects:

```cpp
class Car {
public:
    std::string brand;
    int year;

    void start() {
        std::cout << brand << " is starting..." << std::endl;
    }
};

int main() {
    Car myCar;
    myCar.brand = "Toyota";
    myCar.year = 2020;
    myCar.start();
}
```

- **Encapsulation**: Data hiding using access specifiers (`public`, `private`, `protected`).
- **Inheritance**: Create new classes based on existing ones using the `: public` syntax.
- **Polymorphism**: The ability to process objects differently based on their data type or class (via function overriding and virtual functions).

---

## 7. Memory Management

C++ provides **manual memory management** using pointers and dynamic memory allocation.

### Dynamic Memory Allocation:

```cpp
int* ptr = new int;  // Allocate memory dynamically
*ptr = 100;
std::cout << *ptr << std::endl;
delete ptr;  // Free the allocated memory
```

- **new**: Allocates memory on the heap.
- **delete**: Frees the allocated memory.

C++ also has **smart pointers** (`std::unique_ptr`, `std::shared_ptr`) from the Standard Library to automate memory management.

---

## 8. Templates and Generic Programming

**Templates** allow for generic programming by enabling functions and classes to operate with any data type.

### Function Template:

```cpp
template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    std::cout << add(5, 10) << std::endl;  // Works for integers
    std::cout << add(3.14, 2.72) << std::endl;  // Works for doubles
}
```

### Class Template:

```cpp
template <typename T>
class Box {
public:
    T value;
    Box(T val) : value(val) {}
};

int main() {
    Box<int> intBox(10);
    Box<double> doubleBox(3.14);
}
```

---

## 9. C++ Standard Libraries

The C++ Standard Library provides a rich set of **containers**, **algorithms**, **iterators**, and other utilities:

### Popular Libraries:
- **iostream**: Input/output streams (`std::cout`, `std::cin`)
- **string**: String manipulation (`std::string`)
- **vector**: Dynamic arrays (`std::vector`)
- **algorithm**: Standard algorithms (`std::sort`, `std::find`)
- **map**: Associative containers (`std::map`, `std::unordered_map`)

[Complete Reference to C++ Standard Library](https://en.cppreference.com/w/)

---

## 10. Best Practices

- **Use RAII (Resource Acquisition Is Initialization)** for resource management.
- **Avoid raw pointers**: Use **smart pointers** to prevent memory leaks.
- **Use const**: Prefer `const` wherever possible to improve readability and avoid unintended modifications.
- **Error Handling**: Use **exceptions** to handle errors gracefully.
- **Code modularity**: Write reusable, modular code by splitting functionalities into classes and functions.
- **Optimize code**: Take advantage of C++'s performance features by avoiding unnecessary copies (use **move semantics**).

---

## 11. Learning Resources

- [C++ Programming Language by Bjarne Stroustrup](https://www.stroustrup.com/)
- [LearnCpp](https://www.learncpp.com/)
- [Cplusplus.com](http://www.cplusplus.com/)
- [GeeksforGeeks C++ Tutorials](https://www.geeksforgeeks.org/c-plus-plus

/)

By mastering these C++ features, best practices, and libraries, you can build robust, efficient, and scalable applications across a variety of domains!
# Strings Functions 
Here's the updated table with code examples for each string function in C++:

| **Function**           | **Description**                                                    | **Input Example**            | **Output Example**               | **Code Example**                                                     |
|------------------------|--------------------------------------------------------------------|------------------------------|----------------------------------|----------------------------------------------------------------------|
| `length()` / `size()`   | Returns the number of characters in the string                    | `"Hello"`                    | `5`                              | `string s = "Hello"; cout << s.length();`                            |
| `empty()`              | Checks if the string is empty                                     | `""`                         | `true` (if empty)                | `string s = ""; cout << s.empty();`                                  |
| `clear()`              | Clears the content of the string                                  | `"Hello"`                    | `""`                             | `string s = "Hello"; s.clear(); cout << s;`                          |
| `append()` / `+=`      | Appends a string to the end of the string                         | `"Hello"`, `" World"`        | `"Hello World"`                  | `string s = "Hello"; s.append(" World"); cout << s;`                 |
| `substr()`             | Extracts a substring from the string                              | `"Hello World"`, `0, 5`      | `"Hello"`                        | `string s = "Hello World"; cout << s.substr(0, 5);`                  |
| `find()`               | Finds the first occurrence of a substring or character            | `"Hello World"`, `"World"`   | `6` (position of "World")        | `string s = "Hello World"; cout << s.find("World");`                 |
| `rfind()`              | Finds the last occurrence of a substring or character             | `"Hello World"`, `"o"`       | `7`                              | `string s = "Hello World"; cout << s.rfind('o');`                    |
| `replace()`            | Replaces a portion of the string with another string              | `"Hello World"`, `6, 5, "Everyone"` | `"Hello Everyone"`         | `string s = "Hello World"; s.replace(6, 5, "Everyone"); cout << s;`  |
| `compare()`            | Compares two strings lexicographically                            | `"apple"`, `"banana"`        | `< 0` (apple < banana)           | `string s1 = "apple", s2 = "banana"; cout << s1.compare(s2);`        |
| `c_str()`              | Returns a C-style null-terminated string (`const char*`)          | `"Hello"`                    | `"Hello\0"`                      | `string s = "Hello"; cout << s.c_str();`                             |
| `at()`                 | Returns the character at a specific position (with bounds check)  | `"Hello"`, `1`               | `'e'`                            | `string s = "Hello"; cout << s.at(1);`                               |
| `operator[]`           | Accesses the character at a specific index (no bounds check)      | `"Hello"`, `1`               | `'e'`                            | `string s = "Hello"; cout << s[1];`                                  |
| `insert()`             | Inserts a string or character at a specified position             | `"Hello"`, `5, " World"`     | `"Hello World"`                  | `string s = "Hello"; s.insert(5, " World"); cout << s;`              |
| `erase()`              | Removes a portion of the string                                   | `"Hello World"`, `5, 6`      | `"Hello"`                        | `string s = "Hello World"; s.erase(5, 6); cout << s;`                |
| `push_back()`          | Appends a character to the end of the string                      | `"Hello"`, `'!'`             | `"Hello!"`                       | `string s = "Hello"; s.push_back('!'); cout << s;`                   |
| `pop_back()`           | Removes the last character of the string                          | `"Hello!"`                   | `"Hello"`                        | `string s = "Hello!"; s.pop_back(); cout << s;`                      |
| `begin()` / `end()`    | Returns an iterator to the beginning and end of the string        | `"Hello"`                    | Iterator over `"H", "e", "l",...`| `string s = "Hello"; for(auto it = s.begin(); it != s.end(); ++it) cout << *it;` |
| `rbegin()` / `rend()`  | Returns a reverse iterator to the beginning and end of the string | `"Hello"`                    | Iterator over `"o", "l", "l",...`| `string s = "Hello"; for(auto it = s.rbegin(); it != s.rend(); ++it) cout << *it;`|
| `resize()`             | Resizes the string to a given size                                | `"Hello"`, `8, 'x'`          | `"Helloxxx"`                     | `string s = "Hello"; s.resize(8, 'x'); cout << s;`                   |
| `swap()`               | Swaps the contents of two strings                                 | `"Hello"`, `"World"`         | `"World"`, `"Hello"`             | `string s1 = "Hello", s2 = "World"; s1.swap(s2); cout << s1 << " " << s2;` |
| `find_first_of()`      | Finds the first occurrence of any character from a given set      | `"Hello"`, `"aeiou"`         | `1` (first vowel is 'e')         | `string s = "Hello"; cout << s.find_first_of("aeiou");`              |
| `find_last_of()`       | Finds the last occurrence of any character from a given set       | `"Hello World"`, `"aeiou"`   | `7` (last vowel is 'o')          | `string s = "Hello World"; cout << s.find_last_of("aeiou");`         |
| `find_first_not_of()`  | Finds the first character not in the given set                    | `"Hello World"`, `"Helo "`   | `6` (first 'W')                  | `string s = "Hello World"; cout << s.find_first_not_of("Helo ");`    |
| `find_last_not_of()`   | Finds the last character not in the given set                     | `"Hello World"`, `"dlroW "`  | `4` (last 'o')                   | `string s = "Hello World"; cout << s.find_last_not_of("dlroW ");`    |
| `tolower()`            | Converts a character to lowercase (from `<cctype>`)               | `'H'`                        | `'h'`                            | `char c = 'H'; cout << (char)tolower(c);`                            |
| `toupper()`            | Converts a character to uppercase (from `<cctype>`)               | `'h'`                        | `'H'`                            | `char c = 'h'; cout << (char)toupper(c);`                            |
| `stoi()`               | Converts a string to an integer (`int`)                           | `"123"`                      | `123`                            | `string s = "123"; int num = stoi(s); cout << num;`                  |
| `stol()`               | Converts a string to a `long`                                     | `"123456"`                   | `123456L`                        | `string s = "123456"; long num = stol(s); cout << num;`              |
| `stoll()`              | Converts a string to a `long long`                                | `"1234567890123"`            | `1234567890123LL`                | `string s = "1234567890123"; long long num = stoll(s); cout << num;` |
| `stof()`               | Converts a string to a `float`                                    | `"12.34"`                    | `12.34f`                         | `string s = "12.34"; float num = stof(s); cout << num;`              |
| `stod()`               | Converts a string to a `double`                                   | `"123.456"`                  | `123.456`                        | `string s = "123.456"; double num = stod(s); cout << num;`           |
| `stold()`              | Converts a string to a `long double`                              | `"123.4567890123"`           | `123.4567890123L`                | `string s = "123.4567890123"; long double num = stold(s); cout << num;`|
| `to_string()`          | Converts a numeric value to a string                              | `123`                        | `"123"`                          | `int num = 123; string s = to_string(num); cout << s;`               |

This table now includes code examples demonstrating how to use each function.
