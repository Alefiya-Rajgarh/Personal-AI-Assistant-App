import 'package:flutter/material.dart';

import '../../../../core/widgets/aegis_empty_state.dart';

class SubscriptionScreen extends StatelessWidget {
  const SubscriptionScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Subscription')),
      body: const AegisEmptyState(
        icon: Icons.star_outline,
        title: 'Upgrade available',
        subtitle: 'Unlock premium automation with RevenueCat.',
      ),
    );
  }
}
