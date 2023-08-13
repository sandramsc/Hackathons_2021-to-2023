export const hexToDecimal = (hexadecimal: BigInt) => {
    return parseInt(hexadecimal.toString(), 16);
}

export const decimalToHex = (decimal: number) => {
    return decimal.toString(16);
}