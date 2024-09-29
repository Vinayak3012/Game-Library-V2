#!/usr/bin/bash

# Set the paths (adjust these paths as necessary)
CENTRAL_NODE_MODULES_PATH="/mnt/c/Users/tambe/Documents/VSC/Vue/vue3_master/node_modules" # Path to centralized node_modules
PROJECT_PATH="$(pwd)/frontend"  # Path to the Vue.js project (assuming the script is run in the root folder)
PROJECT_NODE_MODULES_PATH="$PROJECT_PATH/node_modules"

# Step 1: Check if the centralized node_modules exists
if [ ! -d "$CENTRAL_NODE_MODULES_PATH" ]; then
  echo "Error: Centralized node_modules folder does not exist at $CENTRAL_NODE_MODULES_PATH."
  exit 1
fi

# Step 2: Remove existing node_modules folder in the Vue.js project if it exists
if [ -d "$PROJECT_NODE_MODULES_PATH" ]; then
  echo "Removing existing node_modules folder in the Vue.js project..."
  rm -rf "$PROJECT_NODE_MODULES_PATH"
fi

# Step 3: Create a symbolic link from the Vue.js project to the centralized node_modules
echo "Creating symbolic link from $PROJECT_NODE_MODULES_PATH to $CENTRAL_NODE_MODULES_PATH..."
ln -s "$CENTRAL_NODE_MODULES_PATH" "$PROJECT_NODE_MODULES_PATH"

# Step 4: Verify if the symlink was successfully created
if [ -L "$PROJECT_NODE_MODULES_PATH" ]; then
  echo "Symlink created successfully!"
else
  echo "Error: Failed to create the symlink."
  exit 1
fi

# Step 5: Run npm or yarn commands in the Vue.js project (optional)
echo "You can now run npm start or npm run serve in the frontend folder."
