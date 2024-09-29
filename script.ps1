# Define paths
$CENTRAL_NODE_MODULES_PATH = "C:/Users/tambe/Documents/VSC/Vue/vue3_master/node_modules"
$PROJECT_PATH = "C:/Users/tambe/Documents/VSC/Projects/Game_Library/frontend"
$PROJECT_NODE_MODULES_PATH = "$PROJECT_PATH/node_modules"

# Check if the centralized node_modules exists
if (-Not (Test-Path $CENTRAL_NODE_MODULES_PATH)) {
    Write-Host "Error: Centralized node_modules folder does not exist at $CENTRAL_NODE_MODULES_PATH."
    exit 1
}

# Remove existing node_modules folder in the Vue.js project if it exists
if (Test-Path $PROJECT_NODE_MODULES_PATH) {
    Write-Host "Removing existing node_modules folder in the Vue.js project..."
    Remove-Item -Recurse -Force $PROJECT_NODE_MODULES_PATH
}

# Create a symbolic link from the Vue.js project to the centralized node_modules
try {
    New-Item -ItemType SymbolicLink -Path $PROJECT_NODE_MODULES_PATH -Target $CENTRAL_NODE_MODULES_PATH
    Write-Host "Symlink created successfully!"
} catch {
    Write-Host "Error: Failed to create the symlink. $_"
    exit 1
}

Write-Host "You can now run npm start or npm run serve in the project folder."
