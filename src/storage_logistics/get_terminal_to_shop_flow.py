def get_terminal_to_shop_flow(flow_matrix, node_index, terminals, shops, storages):

    result = {}

    for terminal in terminals:
        t_idx = node_index[terminal]
        term_flow = {shop: 0 for shop in shops}
        for storage in storages:
            s_idx = node_index[storage]
            flow_to_storage = flow_matrix[t_idx][s_idx]

            total_out = sum(flow_matrix[s_idx]
                            [node_index[shop]] for shop in shops)
            if total_out == 0:
                continue
            for shop in shops:
                f = flow_matrix[s_idx][node_index[shop]]

                term_flow[shop] += flow_to_storage * f / total_out

        result[terminal] = term_flow
    return result
