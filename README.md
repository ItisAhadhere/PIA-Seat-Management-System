# PIA Flight Management System ✈️

A Python-based GUI simulation for managing seat reservations and cancellations in a PIA airplane, including seat allocation, luggage tracking, and background checks.

## 🚀 Features
- **Seat Reservation & Cancellation** with input validation
- **Three Seat Classes**: Economy, Business, Student
- **Color-coded Seat Map** based on passenger status:
  - 🟢 Clean
  - 🔴 Terrorist
  - 🟠 Unknown
- **Cargo Capacity & Revenue Tracking**
- **Save and Load** reservations (`save_file.save`)
- **State Registry Integration** with `isidata.txt` for ID verification

## 🗂️ Folder Structure
```
pia-flight-management-system/
├── src/
│   ├── main.py           # Main application GUI
│   ├── gencitizens.py    # Generates isidata.txt (5000 citizens with random status)
│   ├── readcitizens.py   # [Optional] For debugging isidata.txt
│   ├── isidata.txt       # Registry file (input for app)
│   └── save_file.save    # Preserves reservation data
├── README.md
├── LICENSE
└── .gitignore
```

## 🛠️ Technologies Used
- Python 3.x
- Tkinter (GUI)
- `pickle` (file handling)
- File I/O

## 🧪 How to Run
```bash
cd src/
python main.py
```
## 👨‍💻 Author

**Abdul Ahad Tanvir**  
📍 Lahore, Pakistan  
📧 itisahadhere@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/abdul-ahad-tanvir-3b14a9283/)

---

⚠️ Notes:
While reserving a seat, ensure the ID field is exactly 7 numeric characters long. The system will reject invalid formats.
Make sure `isidata.txt` and `save_file.save` are present in the same `src/` folder.

## 📄 License
This project is licensed under the MIT License.
