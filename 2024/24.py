def isTreesSynchronized(tree1: dict, tree2: dict) -> list[bool, str]:
    if tree1["value"] != tree2["value"]:
        return [False, tree1["value"]]
    
    try:
        if tree1["right"]["value"] == tree2["left"]["value"] and tree1["left"]["value"] == tree2["right"]["value"]:
            return [True, tree1["value"]]
        
    except KeyError:
        return [True, tree1["value"]]

    return [False, tree1["value"]]


def main():
    tree1 = {
        "value": '🎄',
        "left": { "value": '⭐' },
        "right": { "value": '🎅' }
    }

    tree2 = {
        "value": '🎄',
        "left": { "value": '🎅' },
        "right": { "value": '⭐' },
    }

    print(isTreesSynchronized(tree1, tree2)) # [True, '🎄']

    r"""
    tree1          tree2
    🎄              🎄
    / \             / \
    ⭐   🎅         🎅   ⭐
    """

    tree3 = {
        "value": '🎄',
        "left": { "value": '🎅' },
        "right": { "value": '🎁' }
    }

    print(isTreesSynchronized(tree1, tree3)) # [False, '🎄']

    tree4 = {
        "value": '🎄',
        "left": { "value": '⭐' },
        "right": { "value": '🎅' }
    }

    print(isTreesSynchronized(tree1, tree4)) # [False, '🎄']

    print(isTreesSynchronized(
    { "value": '🎅' },
    { "value": '🧑‍🎄' }
    )) # [False, '🎅']

    print(isTreesSynchronized(
        { "value": "🎄" },
        { "value": "🎄" }
    )) # [True, "🎄"]

    print(isTreesSynchronized(
        { "value": '✨', "left": { "value": '⭐' }, "right": { "value": '🎅' } },
        { "value": '✨', "left": { "value": '🎅' }, "right": { "value": '🎁' } }
    )) # ["False", "✨"]

    print(isTreesSynchronized(
        { "value": "🎁" },
        { "value": "🎁" }
    )) # [True, "🎁"]

    print(isTreesSynchronized(
        { "value": "🎄" },
        { "value": "🎁" }
    )) # [False, "🎄"]

    print(isTreesSynchronized(
        { "value": '🎄', "left": { "value": '⭐' } },
        { "value": '🎄', "right": { "value": '⭐' } }
    )) # [True, "🎄"]

if __name__ == "__main__":
    main()