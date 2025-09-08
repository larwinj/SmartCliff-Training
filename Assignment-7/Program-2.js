const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function Payment_Gateway() {
    let amount = await crw.get("Enter the amount to be paid: ");
    if(amount > 0) {
        console.log(`Payment of ${amount} successful!`);
        return;
    }else{
        console.log("Payment failed.Invalid amount!");
    }
}
async function main(){
    await Payment_Gateway();
    crw.close();
}
main();