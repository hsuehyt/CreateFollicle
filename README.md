### **📌 CreateFollicle**
A Python script for Autodesk Maya that creates a **follicle-based rivet** on a selected face. This is useful for attaching objects (e.g., locators) to deforming geometry, such as rigged characters.

---

## **📥 Installation**
1. **Download the script**:
   - Clone the repository:
     ```sh
     git clone https://github.com/hsuehyt/CreateFollicle.git
     ```
   - Or **Download the `create_follicle_rivet.py` file** directly.

2. **Move the script to your Maya scripts directory**:
   - **Windows:** `C:\Users\YourUser\Documents\maya\scripts`
   - **Mac:** `~/Library/Preferences/Autodesk/maya/scripts`
   - **Linux:** `~/maya/scripts`

---

## **🚀 Usage**
1. **Open Autodesk Maya**.
2. **Select a face** on the mesh where you want to create the follicle.
3. **Run the script in Maya’s Script Editor**:
   ```python
   import create_follicle_rivet
   ```
4. A follicle will be created at the center of the selected face.
5. **Parent your object (e.g., a locator) to the follicle** to make it follow the surface.

---

## **🎯 Features**
✅ Automatically creates a follicle on the selected face  
✅ Connects the follicle properly to the mesh  
✅ Supports animated and deformed meshes  
✅ Works on both **Windows** and **Mac**  

---

## **🛠️ Customizing the Script**
You can manually adjust the follicle's **U/V parameters** in the **Attribute Editor** under `follicleShape` to fine-tune its position.

---

## **📖 Example**
```python
import create_follicle_rivet
```
After running this, a follicle will appear on the selected face.

---

## **🐞 Troubleshooting**
- If the follicle doesn’t attach, ensure your **mesh is not frozen** (`Modify > Freeze Transformations`).
- Try adjusting the **U/V values** in the follicle’s attributes.
- If you don’t see the follicle, check the **Outliner** (`Window > Outliner`).

---

## **📜 License**
This project is open-source and licensed under the **MIT License**.

---

## **📢 Contributing**
Feel free to **fork the repository** and submit pull requests! 🚀