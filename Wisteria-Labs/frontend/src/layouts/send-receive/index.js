import { EthHashInfo } from '@safe-global/safe-react-components';

const Sell = (account) => {
  return <EthHashInfo address={account} showCopyButton />;
};

export default Sell;