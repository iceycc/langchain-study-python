lists = [
    {
        "name": "llm-chain_LCEL",
        "path": "8.1.llm-chain_LCEL.py"
    }, {
        "name": "RouterChain",
        "path": "9.1.RouterChain.py"
    }
]
des = [f"{p['name']}: {p['path']}" for p in lists]
print('\n'.join(des))
