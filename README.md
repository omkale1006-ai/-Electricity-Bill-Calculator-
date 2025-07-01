#⚡ Electricity Bill Calculator 🔢
💡 Developed a smart Electricity Bill Calculator in Python that calculates the bill based on unit consumption using conditionals and exception handling. This mini project enhances logic-building and user input validation skills in Python. ⚡📊  🐍 Technologies: Python, CLI Interface 📂 Project Type: Mini Project | Beginner Level

---

🚀 Features

- 🧾 Bill calculation based on units consumed
- ✅ First 100 units – No charge
- 💸 Next 100 units (101–200) – ₹5 per unit
- 🔺 Above 200 units – ₹10 per unit
- 💡 Input validation using exception handling
- 📟 User-friendly console output with emojis



 🛠️ Tech Stack

- **Language:** Python 🐍  
- **Interface:** Command Line Interface (CLI)



🎯 How It Works

1. User enters the number of units consumed.
2. Program checks slab range:
   - 0–100 units → ₹0
   - 101–200 units → ₹5/unit (for units after 100)
   - 201+ units → ₹10/unit (for units after 200)
3. Displays the final amount with a neat breakdown.



 📷 Demo

```bash
🔌 Welcome to the Electricity Bill Calculator 💡

📄 Billing Rules:
• First 100 units ➡️ No charge
• Next 100 units (101–200) ➡️ ₹5 per unit
• Above 200 units ➡️ ₹10 per unit

🔢 Enter the number of units used: 250
🧮 Calculating your bill...
💰 Chargeable Units: 100 units @ ₹5 = ₹500
💰 Extra Units: 50 units @ ₹10 = ₹500
💰 Total Bill Amount: ₹1000
