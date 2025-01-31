# **Create Follicle on Vertex**
A Python script for **Autodesk Maya** that creates a **follicle-based rivet on a selected vertex**. This allows objects (e.g., locators) to stay attached to deforming geometry, such as rigged characters.

---

## **📥 Installation**
1. **Download the script**:
   - Clone the repository:
     ```sh
     git clone https://github.com/hsuehyt/CreateFollicle.git
     ```
   - Or **Download `create_follicle_on_vertex.py`** directly.

2. **Move the script to your Maya scripts directory**:
   - **Windows:** `C:\Users\YourUser\Documents\maya\scripts`
   - **Mac:** `~/Library/Preferences/Autodesk/maya/scripts`
   - **Linux:** `~/maya/scripts`

---

## **🚀 Usage**
1. **Open Autodesk Maya**.
2. **Select a vertex** on the mesh where you want to create the follicle.
3. **Run the script in Maya’s Script Editor**:
   ```python
   import create_follicle_on_vertex
   ```
4. A **follicle will be created at the selected vertex**.
5. **Parent your object (e.g., a locator) to the follicle** to make it follow the vertex.

---

## **🎯 Features**
✅ Automatically creates a follicle on the selected **vertex**  
✅ Works on **deforming geometry** (e.g., skinned characters)  
✅ Stable even when topology changes  
✅ Works on **Windows, Mac, and Linux**  

---

## **🛠️ How It Works**
- Converts the **selected vertex** into **UV coordinates**.
- Creates a **follicle** at that **UV position**.
- **Connects the follicle** properly to the mesh.
- The follicle **sticks to the vertex**, even if the geometry deforms.

---

## **📖 Example**
```python
import create_follicle_on_vertex
```
After running this, a **follicle will appear at the selected vertex**.

---

## **🐞 Troubleshooting**
- If the follicle doesn’t attach, ensure your **mesh has UVs** (`UV Editor > Layout UVs`).
- Try adjusting the **U/V values** in the follicle’s attributes.
- If you don’t see the follicle, check the **Outliner** (`Window > Outliner`).

---

## **📜 License**
This project is open-source and licensed under the **MIT License**.

---

## **📢 Contributing**
Feel free to **fork the repository** and submit pull requests! 🚀