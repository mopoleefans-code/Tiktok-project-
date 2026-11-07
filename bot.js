const { default: makeWASocket, useMultiFileAuthState } = require('@whiskeysockets/baileys');
const readline = require('readline');

console.log('\n🔄 INITIALIZING MOPOLEE TEXT-CODE PHONE INTERFACE ON ANDROID TERMUX...');

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const question = (text) => new Promise((resolve) => rl.question(text, resolve));

async function startBot() {
    const { state, saveCreds } = await useMultiFileAuthState('auth_session');
    
    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: false
    });

    sock.ev.on('creds.update', saveCreds);

    if (!sock.authState.creds.registered) {
        const phoneNumber = await question('\n📞 ENTER YOUR WHATSAPP NUMBER (Include country code, e.g., 2348123456789): ');
        const cleanNumber = phoneNumber.replace(/[^0-9]/g, '');
        
        console.log('\n🔄 REQUESTING SECURE TEXT ACTIVATION CODE FROM WHATSAPP SERVER...');
        setTimeout(async () => {
            try {
                const code = await sock.requestPairingCode(cleanNumber);
                console.log('\n👑 MOPOLEE ACTIVATION CODE VECTOR LIFT-OFF SUCCESSFUL! 👑');
                console.log(`\n👉 YOUR 8-DIGIT TEXT PAIRING CODE IS: \x1b[32m${code}\x1b[0m \n`);
                console.log('Open WhatsApp -> Linked Devices -> Link with phone number instead and enter this code!\n');
            } catch (err) {
                console.log('\n❌ ERROR REQUESTING CODE: Make sure the number is correct and has country code!');
            }
        }, 3000);
    }

    sock.ev.on('connection.update', (update) => {
        const { connection } = update;
        if (connection === 'open') console.log('\n🟢 SUCCESS: MOPOLEE AI WHATSAPP ONLINE ON AUTOPILOT!\n');
    });

    sock.ev.on('messages.upsert', async (m) => {
        const msg = m.messages[0];
        if (!msg.message || msg.key.fromMe) return;
        const text = (msg.message.conversation || msg.message.extendedTextMessage?.text || '').toLowerCase().trim();
        const from = msg.key.remoteJid;

        if (text === 'hello' || text === 'hi' || text === 'boss' || text === 'baba') {
            await sock.sendMessage(from, { text: '👋 BÀBÁ!!! Welcome to MOPOLEE CINEMA & EXCHANGE!!!\n\nI am your automated AI Business Assistant running 24/7 on autopilot. Type *Shop* to view rates.' });
        } else if (text === 'shop') {
            await sock.sendMessage(from, { text: '💳🛍️ *MOPOLEE LIVE EXCHANGE RATES*:\n\n▪️ Apple Gift Card (\$100): ₦145,000\n▪️ Wholesale MTN SME Data (5GB): ₦1,350' });
        }
    });
}
startBot();
