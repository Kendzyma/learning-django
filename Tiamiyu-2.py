def height(root):
    if (root.left or root.right) is None:
        return 0
    if root.left is None:
        return 1 + height(root.right)
    if root.right is None:
        return 1 + height(root.left)
    return 1 + max(height(root.left), height(root.right))