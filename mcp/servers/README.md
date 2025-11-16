Run server locally
'''
DOTENV_PATH=/c/Users/ruban/.env LOG_LEVEL=info  fastmcp run mcp/servers/gemini_media_gen.py
'''
Install on gemini
'''
fastmcp install gemini-cli mcp/servers/gemini_media_gen.py --with-requirements mcp/requirements.txt
'''

